IDENTITY_CERT_PASSWORD := $(shell jq -r '.IDENTITY_CERT_PASSWORD' config.json)
SERVICE_HTTP_PORT := $(shell jq -r '.SERVICE_HTTP_PORT' config.json)
SERVICE_HTTPS_PORT := $(shell jq -r '.SERVICE_HTTPS_PORT' config.json)

SERVICE_URI_ORIGINAL := $(shell jq -r '.SERVICE_URI' config.json)
# Remove "http://" or "https://" from the beginning of the URL
SERVICE_URI := $(SERVICE_URI_ORIGINAL:http://%=%)
SERVICE_URI := $(SERVICE_URI:https://%=%)

OPENSSL_CONFIG := openssl_config.cnf

$(OPENSSL_CONFIG):
	printf '[req]\nreq_extensions = v3_req\n\n[v3_req]\nsubjectAltName = @alt_names\n\n[alt_names]\nDNS.1 = $(SERVICE_URI)\n' > $@

# run this step if you want to cleanup everything
clean:
	docker-compose -f ./bwdata/docker/docker-compose.yml down
	rm -f docker-stub.zip
	find bwdata -mindepth 1 -maxdepth 1 -type d -print0 | xargs -r0 rm -rf

# run this step only 1 time
install: $(OPENSSL_CONFIG)
	# Step 1
	curl -L https://github.com/bitwarden/server/releases/download/v2024.2.2/docker-stub-EU.zip -o docker-stub.zip

	# Step 2
	unzip docker-stub.zip -d bwdata

	# Step 4
	openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout ./bwdata/identity/identity.key -out ./bwdata/identity/identity.crt -subj "/CN=Bitwarden IdentityServer" -days 10950
	openssl pkcs12 -export -out ./bwdata/identity/identity.pfx -inkey ./bwdata/identity/identity.key -in ./bwdata/identity/identity.crt -passout pass:$(IDENTITY_CERT_PASSWORD)
	
	# Step 5
	cp ./bwdata/identity/identity.pfx ./bwdata/ssl/identity.pfx

	# Step 6
	mkdir ./bwdata/ssl/$(SERVICE_URI)

	# Step 7
	openssl req -x509 -newkey rsa:4096 -sha256 -nodes -days 365 \
        -keyout ./bwdata/ssl/$(SERVICE_URI)/private.key \
        -out ./bwdata/ssl/$(SERVICE_URI)/certificate.crt \
        -config $(OPENSSL_CONFIG) \
        -subj "/C=RO/ST=Bucharest/L=Bucharest/O=HOMELAB/OU=Bitwarden/CN=$(SERVICE_URI)"
	rm -f $(OPENSSL_CONFIG)

	$(MAKE) apply_config

# you can run this step multiple times
apply_config:
	# Step 3 & 9
	python3 update_env.py

	# Step 8
	python3 update_nginx.py ./bwdata/nginx/default.conf bitwarden.example.com $(SERVICE_URI)

	# Step 10
	jq '.trustedFacets[0].ids[0] = "$(SERVICE_URI_ORIGINAL)"' ./bwdata/web/app-id.json > temp.json && mv temp.json ./bwdata/web/app-id.json

	# Step 11
	echo "LOCAL_UID=$(shell id -u)" > ./bwdata/env/uid.env
	echo "LOCAL_GID=$(shell id -g)" >> ./bwdata/env/uid.env

	# Change published docker ports
	sed -i 's/80:8080/$(SERVICE_HTTP_PORT):8080/g' ./bwdata/docker/docker-compose.yml
	sed -i 's/443:8443/$(SERVICE_HTTPS_PORT):8443/g' ./bwdata/docker/docker-compose.yml

restart: apply_config
	docker-compose -f ./bwdata/docker/docker-compose.yml restart

run:
	docker-compose -f ./bwdata/docker/docker-compose.yml up -d