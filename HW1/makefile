SCRIPT=RobertoRamil_hw01-p1.py
RUNDIR=run
CMDLINE=
HOME=${PWD}

all: ${RUNDIR}
	@clear
	@echo Running python code ${SCRIPT}\; check "Output" tab for results.
	@echo
	cd ${RUNDIR} && \
	python3 '${HOME}/${SCRIPT}' ${CMDLINE}
	@echo
	@echo ... done.

${RUNDIR}:
	@echo Creating directory ${RUNDIR}.
	mkdir -p ${RUNDIR}

clean:
	@echo Deleting file in ${RUNDIR} and removing the folder.
	rm -rf ${RUNDIR}/*
	rmdir ${RUNDIR}d