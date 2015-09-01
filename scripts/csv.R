INFILE = '/home/gabe/projects/ideology/data/Polarization 2014 public.sav'
OUTFILE = '/home/gabe/projects/ideology/data/rawdata.csv'

library(foreign)
dataset = read.spss(INFILE, to.data.frame=TRUE)
write.csv(file=OUTFILE, x=dataset)