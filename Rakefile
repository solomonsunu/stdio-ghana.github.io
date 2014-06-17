# courtesy of guidance at http://davidensinger.com/
#require 'bundler/setup'
require 'reduce'

task :default => 'all'

desc "build _site/"
task :build do
  puts system("jekyll build") ? "Success" : "Failed"
end

desc "minimize images"
task :minimize do
  puts "\n## Compressing static assets"
  original = 0.0
  compressed = 0
  Dir["**/*.*"].reject{ |f| f['_site/'] }.each do |file|
    case File.extname(file)
      when ".gif", ".jpg", ".jpeg", ".png"
        puts "Processing: #{file}"
        original += File.size(file).to_f
        min = Reduce.reduce(file)
        File.open(file, "w") do |f|
          f.write(min)
        end
        compressed += File.size(file)
      end
  end
  puts "Total compression %0.2f\%" % (((original-compressed)/original)*100)
end

desc "commit _site/"
task :commit do
  puts "\n## Staging modified files"
  puts system("git add -A") ? "Success" : "Failed"
  puts "\n## Committing a site build at #{Time.now.utc}"
  puts system("git commit -m \"Build site at #{Time.now.utc}\"") ? "Success" : "Failed"
  puts "\n## Pushing commits to remote"
  puts system("git push origin source") ? "Success" : "Failed"
end

desc "deploy _site/"
task :deploy do
  puts "\n## Deleting master branch"
  puts system("git branch -D master") ? "Success" : "Failed"
  puts "\n## Creating new master branch and switching to it"
  puts system("git checkout -b master") ? "Success" : "Failed"
  puts "\n## Forcing the _site subdirectory to be project root"
  puts system("git filter-branch --subdirectory-filter _site/ -f") ? "Success" : "Failed"
  puts "\n## Switching back to source branch"
  puts system("git checkout source") ? "Success" : "Failed"
  puts "\n## Pushing all branches to origin"
  puts system("git push --all origin") ? "Success" : "Failed"
end

desc "build, commit, and deploy _site/"
task :all => [:build, :minimize, :commit, :deploy] do
end
