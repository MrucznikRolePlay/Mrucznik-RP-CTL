import os
import json


def check_configuration(args):
    assert(os.path.isdir('./modules'))
    assert(os.path.exists('./modules/modules.json'))
    # all modules in modules.json check
    with open('./modules/modules.json') as modules_json:
        json_data = json.load(modules_json)
        for modules in json_data['modules']:
            module_name = modules['name']
            module_filename = './modules/{0}/{0}.json'.format(module_name)
            assert(os.path.isdir('./modules/{}'.format(module_name)))
            assert(os.path.exists(module_filename))
            with open(module_filename) as module_file:
                module_json = json.load(module_file)
                assert(os.path.isdir('./modules/{}/commands'.format(module_name)))
                for command in module_json['commands']:
                    command_name = command['name']
                    assert(os.path.isdir('./modules/{}/commands/{}'.format(module_name, command_name)))
                    assert(os.path.exists('./modules/{0}/commands/{1}/{1}.json'.format(module_name, command_name)))

    print('all ok')
    # TODO: checking for unlisted files
