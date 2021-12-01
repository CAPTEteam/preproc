"""
Command line interface for the preproc module.
"""
import argparse
import logging
import sys

import preproc
from . import preproc
from . import cliutils


_LOGGER = logging.getLogger(__name__)


def create_parser():
	"""
	Create the parser for the preproc command.

	:return: Configured parser.
	:rtype: argparse.ArgumentParser
	"""
	parser = argparse.ArgumentParser(
		description='''
Pre_processing
'''
		)
	
	parser.add_argument(
		'input_folder',
		type=cliutils.sanitize_path,
		help='Directory of the session you want to proces ex: "/mnt/PROCESSDATA/TEMP_TEST_DEV/Simon_test/Session 2021-02-22 09-44-37/" '
		)


	parser.add_argument(
		'configuration_file',
		type=cliutils.sanitize_path,
		help='Configuration file for the modules ex : "/home/capte-gpu-1/Documents/espaces_personnel/SIMON/modules_Arvalis/yellowgreen-multi/config/yellowConfiguration.json" '
		)

	# Optional arguments
	cliutils.add_boolean_flag(parser, 'debug', 'Enable debug outputs. Imply --verbose.')
	cliutils.add_boolean_flag(parser, 'verbose', 'Enable debug logging.')

	return parser

def main(args=None):
	"""
	Run the main procedure.

	:param list args: List of arguments for the command line interface. If not set, arguments are
		taken from ``sys.argv``.
	"""
	parser = create_parser()
	args = parser.parse_args(args)
	args.verbose = args.verbose or args.debug

	# Ensure the directory exists to create the log file
	#args.output_folder.mkdir(parents=True, exist_ok=True)
	#log_filename = args.output_folder.joinpath('preproc.log')

	#cliutils.setup_logging(debug=args.verbose, filename=log_filename)
	#_LOGGER.debug('command: %s', ' '.join(sys.argv))
	#_LOGGER.debug('version: %s', preproc.__version__)

	# Call the main function of the module
	preproc.princ(args.input_folder, args.configuration_file)


if __name__ == '__main__':
	main()
