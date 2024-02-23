import json

def update_env_file(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)

    mapping = {
        "SERVICE_URI": [
            { "property": "globalSettings__baseServiceUri__vault", "file": "./bwdata/env/global.override.env" }
        ],
        "SERVICE_REGION": [
            { "property": "globalSettings__baseServiceUri__cloudRegion", "file": "./bwdata/env/global.override.env" }
        ],

        "RANDOM_DATABASE_PASSWORD": [
            { "property": "globalSettings__sqlServer__connectionString", "file": "./bwdata/env/global.override.env", "replace_substring": True },
            { "property": "SA_PASSWORD", "file": "./bwdata/env/mssql.override.env" }
        ],

        "IDENTITY_CERT_PASSWORD": [
            { "property": "globalSettings__identityServer__certificatePassword", "file": "./bwdata/env/global.override.env" }
        ],
        "RANDOM_IDENTITY_KEY": [
            { "property": "globalSettings__internalIdentityKey", "file": "./bwdata/env/global.override.env" },
            { "property": "globalSettings__oidcIdentityClientKey", "file": "./bwdata/env/global.override.env" }
        ],
        "RANDOM_DUO_AKEY": [
            { "property": "globalSettings__duo__aKey", "file": "./bwdata/env/global.override.env" }
        ],

        "SECRET_INSTALLATION_ID": [
            { "property": "globalSettings__installation__id", "file": "./bwdata/env/global.override.env" }
        ],
        "SECRET_INSTALLATION_KEY": [
            { "property": "globalSettings__installation__key", "file": "./bwdata/env/global.override.env" }
        ],

        "MAIL_REPLY_EMAIL": [
            { "property": "globalSettings__mail__replyToEmail", "file": "./bwdata/env/global.override.env" }
        ],
        "MAIL_SMTP_HOST": [
            { "property": "globalSettings__mail__smtp__host", "file": "./bwdata/env/global.override.env" }
        ],
        "MAIL_SMTP_PORT": [
            { "property": "globalSettings__mail__smtp__port", "file": "./bwdata/env/global.override.env" }
        ],
        "MAIL_SMTP_SSL": [
            { "property": "globalSettings__mail__smtp__ssl", "file": "./bwdata/env/global.override.env" }
        ],
        "MAIL_SMTP_USER": [
            { "property": "globalSettings__mail__smtp__username", "file": "./bwdata/env/global.override.env" }
        ],
        "MAIL_SMTP_PASS": [
            { "property": "globalSettings__mail__smtp__password", "file": "./bwdata/env/global.override.env" }
        ],
    }

    for config_key, config_value in config.items():
        if config_key in mapping:
            for entry in mapping[config_key]:
                property_name = entry["property"]
                env_file = entry["file"]
                replace_substring = entry.get("replace_substring", False)
                
                with open(env_file, 'r') as f:
                    lines = f.readlines()

                with open(env_file, 'w') as f:
                    for line in lines:
                        if line.startswith(property_name + "="):
                            if replace_substring:
                                existing_value = line.replace(property_name + "=", "").rstrip("\n")
                                new_value = existing_value.replace(config_key, config_value)
                                f.write(f"{property_name}={new_value}\n")
                            else:
                                f.write(f"{property_name}={config_value}\n")
                        else:
                            f.write(line)

                print(f"Updated '{property_name}' in '{env_file}' to '{config_value}'")

if __name__ == "__main__":
    update_env_file("config.json")
