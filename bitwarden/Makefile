clean:
	rm -f docker-stub.zip
	find bwdata -mindepth 1 -maxdepth 1 -type d -print0 | xargs -r0 rm -rf

install:
	curl -L https://github.com/bitwarden/server/releases/download/v2024.2.2/docker-stub-EU.zip -o docker-stub.zip
	unzip docker-stub.zip -d bwdata