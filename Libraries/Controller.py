import sys

from Http import Http
from Logger import Logger as log
from Progress import Progress
from Version import Version


class Controller:
	"""Controller class"""

	DEFAULT_LOGGING = False

	def __init__(self, InputArguments):
		"""

        :type InputArguments: Dict[str, str]
        """
		func_call = {'url': self.url_action, 'update': self.update_action, 'version': self.version_action}
		for action, args in InputArguments.iteritems():
			# TODO  add debug
			# try:
			# dynamic function call
			if not args:
				func_call[action]()
			# getattr(self, '{func}_action'.format(func=action))()
			else:
				func_call[action](args, InputArguments)
			# # getattr(self, '{func}_action'.format(func=action))(args, InputArguments)
			#    self.url_action(args,InputArguments)
			#    break

			# except AttributeError:
			# log.critical(action + """ action does not exist in Controller""")

	@staticmethod
	def update_action():
		""" Update action """
		# TODO this function is not exists, DON'T USE IT
		# Version.update()
		log.critical("this function is not exists, DON'T USE IT")
		exit()

	@staticmethod
	def version_action():
		""" Show version action """

		sys.exit(Version().get_full_version())

	def url_action(self, url, params=()):
		""" Load by url action """

		result = Http().get(url, params)
		if result:
			Progress.view(result)
			is_logging = params.get('log', self.DEFAULT_LOGGING)

			if is_logging:
				log.syslog(url, result)
		exit()

	@staticmethod
	def examples_action():
		""" Show examples action """

		examples = """
            Examples:
                python ./opendoor.py  --examples
                python ./opendoor.py  --update
                python ./opendoor.py  --version
                python ./opendoor.py --url "http://joomla-ua.org"
                python ./opendoor.py --url "http://joomla-ua.org" --check subdomains
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10 --proxy
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10 --delay 10
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10 --delay 10 --rest 10
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10 --delay 10 --rest 10 --debug 1
                python ./opendoor.py --url "http://joomla-ua.org" --threads 10 --delay 10 --rest 10 --debug 1 --log
            """
		exit(examples)
