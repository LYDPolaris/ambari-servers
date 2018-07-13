# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from resource_management.core.exceptions import ClientComponentHasNoStatus
from resource_management.core.resources.system import Execute
from resource_management.libraries.script.script import Script


class Cli(Script):
    def install(self, env):
        import params
        env.set_params(params)
        # Install dependent packages
        self.install_packages(env)

        Execute('rm -rf /usr/lib/presto/bin')
        # Create Presto directories
        Directory(['/usr/lib/presto/bin'],
                  mode=0755,
                  cd_access='a',
                  owner=params.presto_user,
                  group=params.presto_group,
                  create_parents=True
                  )
        Execute('wget --no-check-certificate {0} -O /usr/lib/presto/bin/presto-cli'.format(params.presto_cli_download_url, params.presto_base_dir))
        Execute('chmod +x /usr/lib/presto/bin/presto-cli')

    def status(self, env):
        raise ClientComponentHasNoStatus()

    def configure(self, env):
        import params
        env.set_params(params)

    def start(self, env):
        import params
        env.set_params(params)

    def stop(self, env):
        import params
        env.set_params(params)

if __name__ == '__main__':
    Cli().execute()