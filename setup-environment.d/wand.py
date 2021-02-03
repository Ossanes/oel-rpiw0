def __set_defaults_freedom_yocto():
    set_default('MACHINE', 'wandboard')
    set_default('DISTRO', 'fel')
    set_default('SDKMACHINE', 'x86_64')


def __after_init_freedom_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-aquino',
                        'meta-openembedded/meta-networking',
                        'meta-openembedded/meta-oe',
                        'meta-openembedded/meta-python',
                        'meta-freescale-3rdparty',
			'meta-freescale',
                    ]])


run_set_defaults(__set_defaults_freedom_yocto)
run_after_init(__after_init_freedom_yocto)
