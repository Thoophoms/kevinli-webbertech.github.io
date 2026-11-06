const { execFileSync } = require('node:child_process');
const { writeFileSync } = require('node:fs');
const { join } = require('node:path');
const root = join(__dirname, '..');
const records = execFileSync('git', ['log', '-5', '--format=%h%x09%cI%x09%s'], { cwd: root, encoding: 'utf8' });
const commits = records.trim().split('\n').filter(Boolean).map(line => {
  const [sha, date, ...subject] = line.split('\t');
  return { sha, date, message: subject.join('\t') };
});
writeFileSync(join(root, 'js', 'latest-changes.json'), JSON.stringify(commits, null, 2) + '\n');
