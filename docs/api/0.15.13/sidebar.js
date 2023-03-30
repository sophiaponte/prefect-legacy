const glob = require('glob')

// function for loading all MD files in a directory
const getChildren = function (parent_path, dir) {
    return glob
        .sync(parent_path + '/' + dir + '/**/*.md')
        .map(path => {
            // remove "parent_path" and ".md"
            path = path.slice(parent_path.length + 1, -3)
            // remove README
            if (path.endsWith('README')) {
                path = path.slice(0, -6)
            }
            return path
        })
        .sort()
}

sidebar = [
    {
        title: 'API Reference',
        path: '/api/0.15.13/'
    },
      'changelog',
      {
        title: 'prefect',
        collapsable: true,
        children: ['triggers']
      },
      {
        title: 'prefectlegacy.backend',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'backend')
      },
      {
        title: 'prefectlegacy.client',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'client')
      },
      {
        title: 'prefectlegacy.cli',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'cli')
      },
      {
        title: 'prefectlegacy.core',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'core')
      },
      {
        title: 'prefectlegacy.engine',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'engine')
      },
      {
        title: 'prefectlegacy.environments',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'environments')
      },
      {
        title: 'prefectlegacy.executors',
        collapsable: true,
        children: ['executors.md']
      },
      {
        title: 'prefectlegacy.run_configs',
        collapsable: true,
        children: ['run_configs.md']
      },
      {
        title: 'prefectlegacy.storage',
        collapsable: true,
        children: ['storage.md']
      },
      {
        title: 'prefectlegacy.tasks',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'tasks')
      },
      {
        title: 'prefectlegacy.schedules',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'schedules')
      },
      {
        title: 'prefectlegacy.agent',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'agent')
      },
      {
        title: 'prefectlegacy.utilities',
        collapsable: true,
        children: getChildren('docs/api/0.15.13', 'utilities')
      }
]

module.exports = {sidebar: sidebar}