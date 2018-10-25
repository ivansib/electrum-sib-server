from setuptools import setup

setup(
    name="electrum-sibcoin-server",
    version="1.0",
    scripts=['run_electrum_sibcoin_server','electrum-sibcoin-server'],
    install_requires=['plyvel', 'jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumserver': 'src'
    },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Sibcon Electrum Server",
    author="Thomas Voegtlin ,ELM4ever, Propulsion, TheLazieR",
    author_email="thomasv@electrum.org, thelazier@gmail.com",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/thelazier/electrum-dash-server/, https://github.com/ivansib/electrum-sib-server",
    long_description="""Server for the Electrum Lightweight Sibcoin Wallet"""
)
