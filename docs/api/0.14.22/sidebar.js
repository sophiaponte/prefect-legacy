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
        path: '/api/0.14.22/'
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
        children: getChildren('docs/api/0.14.22', 'backend')
    },
    {
        title: 'prefectlegacy.client',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'client')
    },
    {
        title: 'prefectlegacy.cli',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'cli')
    },
    {
        title: 'prefectlegacy.core',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'core')
    },
    {
        title: 'prefectlegacy.engine',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'engine')
    },
    {
        title: 'prefectlegacy.environments',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'environments')
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
        children: getChildren('docs/api/0.14.22', 'tasks')
    },
    {
        title: 'prefectlegacy.schedules',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'schedules')
    },
    {
        title: 'prefectlegacy.agent',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'agent')
    },
    {
        title: 'prefectlegacy.artifacts',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'artifacts')
    },
    {
        title: 'prefectlegacy.utilities',
        collapsable: true,
        children: getChildren('docs/api/0.14.22', 'utilities')
    }
]

module.exports = {sidebar: sidebar}