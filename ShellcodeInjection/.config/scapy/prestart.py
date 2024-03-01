# Scapy CLI 'pre-start' config file
# see https://scapy.readthedocs.io/en/latest/api/scapy.config.html#scapy.config.Conf
# for all available options

# default interpreter
conf.interactive_shell = "auto"

# color theme (DefaultTheme, BrightTheme, ColorOnBlackTheme, BlackAndWhite, ...)
conf.color_theme = DefaultTheme()

# disable INFO: tags related to dependencies missing
# log_loading.setLevel(logging.WARNING)

# force-use libpcap
# conf.use_pcap = True