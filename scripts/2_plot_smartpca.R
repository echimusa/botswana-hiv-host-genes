#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)

library(dplyr)
library(ggplot2)
#library(grid)
#library(gridExtra)
library(RColorBrewer)

# Open empty pdf file for plotting
png(args[3]) #, width=7, height=8)

# Reading eigenvalues file
eval <- read.table(args[1])

evec1.pc <- round(eval[1,1]/sum(eval)*100,digits=2)
evec2.pc <- round(eval[2,1]/sum(eval)*100,digits=2)

# Reading eigenvectors file
evec <- read.table(args[2],col.names=c("Sample", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6", "PC7", "PC8", "PC9", "PC10", "Population")) #,header=T)
attach(evec)
x<- c(0,1,2,3,4,5,8,15,16,17,18)
symb <- sample(x,nrow(evec), replace = TRUE)
evec <-dplyr::mutate (evec, symbol = symb)

xlab <- paste("\n\n",evec1.pc, "% of observed genetic variation (PC1)", sep="")
ylab <- paste("\n",evec2.pc, "% of observed genetic variation (PC2)", sep="")

col2 <- c("black", "blue","cyan", "brown","rosybrown",  "olivedrab", "navy",  "lavender", "gold", "firebrick",  "dodgerblue","forestgreen","black","coral", "chartreuse", "chocolate","red","tomato","turquoise","violet","yellow","sienna","seagreen","salmon","plum","purple", "red","pink","orange","green" ,"maroon","magenta") 

My_Theme = theme(
  axis.title.x = element_text(size = 16),
  axis.text.x = element_text(size = 14,face="bold"),
  axis.title.y = element_text(size = 16,face="bold"))

p <- ggplot(evec,aes(x=PC1,y=PC2)) #+ scale_color_viridis()

p <- p+geom_point(aes(color=Population,pch=Population),alpha = 2.5,stroke=3.4) + xlab(xlab) + ylab(ylab) ##+scale_x_log10()
p <- p +  theme_light(base_size = 2.5) + theme(panel.grid.minor = element_blank()) + My_Theme
jit <- position_jitter(seed = 123)  
p <- p +  geom_jitter(aes(shape = Population, color = Population),size =1.5,position = jit) + scale_shape_manual(values = evec$symbol)
p <- p+scale_colour_manual(values = col2)+ theme(legend.position = "bottom")
plot.new()
par(mar=rep(0, 4))
p <- p + theme(legend.box.just = "left",panel.background = element_rect(fill = 'grey75'),panel.grid.major = element_line(colour = "orange", size=0.5), panel.grid.minor = element_line(colour = "blue"),legend.title=element_text(size=7.5),legend.text=element_text(size=rel(7.5)))
dev.off()
