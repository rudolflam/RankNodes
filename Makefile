default:
	@echo "None";
install_graphtools:
	chmod +x ./install_graphtools.sh
	./install_graphtools.sh
install: 
	pip2 install .
install_all: install_graphtools install
	@echo "Installing "
uninstall:
	pip2 uninstall ranknodes
	
