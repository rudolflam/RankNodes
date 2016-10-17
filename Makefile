default:
	@echo "None";
install_graphtools:
	chmod +x ./install_graphtools.sh
	./install_graphtools.sh
install: install_graphtools
	@echo "Installing "
	sudo pip2 install .
uninstall:
	sudo pip2 uninstall ranknodes
	