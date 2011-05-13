pyvows:
	@env PYTHONPATH=$$PYTHONPATH:. pyvows --cover --cover_package=django_bigpipe --cover_threshold=100 vows/
