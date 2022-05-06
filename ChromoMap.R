library(chromoMap)
chr_file = "C:/Path/wheat_chr.txt"
anno_file = "C:/Path/wheat_gene.txt"
head(read.table(chr_file,sep = "\t"))
head(read.table(anno_file,sep = "\t"))
chromoMap(list(chr_file),list(anno_file))
chromoMap(chr_file,anno_file, data_based_color_map = T,
          data_type = "numeric", legend = T, data_colors = list(c("red","blue")), lg_x = 0,
          lg_y = 300, chr_color = c("grey"), win.summary.display=T)
