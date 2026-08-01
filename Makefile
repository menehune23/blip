.PHONY: package
package:
	python3 scripts/update_manifests.py

.PHONY: install
install:
	python3 -m mpremote mip install package.local.json

.PHONY: install-remote
install-remote:
	python3 -m mpremote mip install github:menehune23/blip@$$(git rev-parse --abbrev-ref HEAD)

.PHONY: dev
dev: package install
