# # Set configuration
# git config --global user.email "builduser@dummy.local"
# git config --global user.name "Build user"

# # Select a branch
# git checkout UPDATES_&_Udemy_Angela_4romD7 2>&1 | write-host

# # Get the current status
# $status = git status 2>&1 | write-host

# Stage the changes
git add . 2>&1 | write-host

# Commit the changes
git commit -m "Automated Repo Update" 2>&1 | write-host

# Push the changes to the remote repository
git push 2>&1 | write-host

# # Get the final status
# $pushStatus = git status 2>&1 | write-host
git status
# # Display the status messages
# write-host $status
# write-host $pushStatus