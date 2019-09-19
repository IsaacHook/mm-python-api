# ----------------------------------------------------------------------------
# Get branch and release information.
CURRENT_BRANCH = $(shell git branch | grep \* | cut -d ' ' -f2)
VERSION = $(shell cat version.txt)
RELEASE_BRANCH = release/${VERSION}

.PHONY: develop release

develop:
ifneq (${CURRENT_BRANCH},develop)
	@echo "Switching to branch develop..."
	@git pull
	@git checkout develop
	@echo Done - mm-python-api
endif

release:
ifneq (${CURRENT_BRANCH},${RELEASE_BRANCH})
	@echo "Switching to branch ${RELASE_BRANCH}"
	@git pull
	@git checkout ${RELEASE_BRANCH}
	@echo Done - mm-python-api
endif

