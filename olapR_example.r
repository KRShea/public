
library(olapR)

setwd("")

SummaryDataOldHGA <- read.csv("HistoricSummaryData_CurrentHGA.csv")
SummaryDataOldCAS <- read.csv("HistoricSummaryData_CurrentCAS.csv")
SummaryDataOldLOWE <- read.csv("HistoricSummaryData_CurrentLOWE.csv")
SummaryDataOldMIA <- read.csv("HistoricSummaryData_CurrentMIA.csv")

oldfilenameHGA <- gsub(" ","_", paste("HistoricSummaryDataHGA_",SummaryDataOldHGA$Timestamp[1],".csv", sep = "") )
oldfilenameCAS <- gsub(" ","_", paste("HistoricSummaryDataCAS_",SummaryDataOldCAS$Timestamp[1],".csv", sep = "") )
oldfilenameLOWE <- gsub(" ","_", paste("HistoricSummaryDataLOWE_",SummaryDataOldLOWE$Timestamp[1],".csv", sep = "") )
oldfilenameMIA <- gsub(" ","_", paste("HistoricSummaryDataMIA_",SummaryDataOldMIA$Timestamp[1],".csv", sep = "") )

oldfilenameHGA <- gsub(":",".",oldfilenameHGA)
oldfilenameCAS <- gsub(":",".",oldfilenameCAS)
oldfilenameLOWE <- gsub(":",".",oldfilenameLOWE)
oldfilenameMIA <- gsub(":",".",oldfilenameMIA)

write.csv(SummaryDataOldHGA, file = oldfilenameHGA, row.names=FALSE)
write.csv(SummaryDataOldCAS, file = oldfilenameCAS, row.names=FALSE)
write.csv(SummaryDataOldLOWE, file = oldfilenameLOWE, row.names=FALSE)
write.csv(SummaryDataOldMIA, file = oldfilenameMIA, row.names=FALSE)


### Create connection string and execute MDX Query 

cnnstr <- "Provider=MSOLAP;Data Source= servername ;Persist Security Info=False;Integrated Security=SSPI;Initial Catalog=Finance_FDM"
 
olapCnn <- OlapConnection(cnnstr)

mdx <- " Query "
	
dataset <- execute2D(olapCnn, mdx)	

## Remove columns containing Member Unique Name

dataset <-  dataset[ , grep("MEMBER_UNIQUE_NAME",colnames(dataset),invert=TRUE)]

### Remove redundancy from column names

colnames2 <- gsub("\\[MEMBER_CAPTION]","",colnames(dataset))

colnames2 <- gsub("\\[Measures]","",colnames2)

colnames2 <- gsub("\\.","",colnames2)

bracketlist <- gregexpr("\\[", colnames2)

bracketlist2 <- lapply(bracketlist, function(x) x[which.max(abs(x))])

bracketvector <- unlist(bracketlist2)

### replace column names


colnames(dataset) <-  substr(colnames2,bracketvector,999)

#Remove Special Characters and Spaces
colnames(dataset) <- gsub("-","",colnames(dataset))
colnames(dataset) <- gsub("  ","_",colnames(dataset))
colnames(dataset) <- gsub(" ","_",colnames(dataset))
colnames(dataset) <- gsub("&","",colnames(dataset))
colnames(dataset) <- gsub("\\[","",colnames(dataset))
colnames(dataset) <- gsub("\\]","",colnames(dataset))




Quarter <- ifelse( substr(dataset$Fiscal_Month_Name,1,2) %in% c("01","02","03"),"Q1",
				ifelse(substr(dataset$Fiscal_Month_Name,1,2) %in% c("04","05","06"),"Q2",
					ifelse(substr(dataset$Fiscal_Month_Name,1,2) %in% c("07","08","09"),"Q3",
						ifelse(substr(dataset$Fiscal_Month_Name,1,2) %in% c("10","11","12"),"Q4","Error"))))
					
					
dataset <- cbind(Quarter,dataset)
					
dataset$Variance = dataset$Management_FPA_Mangement_Budget_Amount - dataset$Management_FPA_MTD_Amount

dataset$Timestamp <-  Sys.time()

dataset$WD_Driver_Tag_Description <- gsub("[\r\n]", "", dataset$WD_Driver_Tag_Description)


write.csv(dataset, file = "HistoricSummaryData_Current.csv",row.names=FALSE)

write.csv(dataset[which(dataset$Level_04_Budget_Unit == "Level 04 - Miami Institute for Advanced Study of the Americas (MIA)"),], file = "HistoricSummaryData_CurrentMIA.csv",row.names=FALSE)

write.csv(dataset[which(dataset$Level_04_Budget_Unit == "Level 04 - College Of Arts & Sciences"),], file = "HistoricSummaryData_CurrentCAS.csv",row.names=FALSE)

write.csv(dataset[which(dataset$Level_04_Budget_Unit == "Level 04 - Lowe Art Museum"),], file = "HistoricSummaryData_CurrentLOWE.csv",row.names=FALSE)

write.csv(dataset[which(dataset$Level_04_Budget_Unit == "Level 04 - Hemispheric and Global Affairs"),], file = "HistoricSummaryData_CurrentHGA.csv",row.names=FALSE)

###
###
