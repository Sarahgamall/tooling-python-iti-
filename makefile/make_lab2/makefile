include config.mk

allObjs = $(fileObj1) $(fileObj2) $(fileObj3) $(fileObj4) $(fileObj5) $(fileObj6)

$(FinalTargetName): CFLAG = 
$(allObjs): CFLAG = -c

$(FinalTargetName): $(allObjs)
	$(CC) $(CFLAG) $^ -o $@ 

$(fileObj1) : $(fileSrc1) 
	$(CC) $(CFLAG) $^ -o $@
$(fileObj2) : $(fileSrc2) 
	$(CC) $(CFLAG) $^ -o $@
$(fileObj3) : $(fileSrc3) 
	$(CC) $(CFLAG) $^ -o $@ 
$(fileObj4) : $(fileSrc4) 
	$(CC) $(CFLAG) $^ -o $@ 
$(fileObj5) : $(fileSrc5) 
	$(CC) $(CFLAG) $^ -o $@
$(fileObj6) : $(fileSrc6) 
	$(CC) $(CFLAG) $^ -o $@

.PHONY : clean link onlyCompile

clean: 
	DEL $(FinalTargetName) $(allObjs) 

link: 
	$(CC) $(allObjs) -o $(FinalTargetName) 

onlyCompile: $(allObjs)
