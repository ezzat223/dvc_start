# Commands

```bash
# Display the DVC version and system/environment information.
dvc version (doctor)

dvc init             # Initialize DVC repository.
dvc add              # Track data files or directories with DVC (git add).
dvc commit           # Record changes to files or directories tracked by DVC by storing the current versions in the cache.
dvc pull             # Download tracked files or directories from remote storage (we run it after: git clone or git pull).
dvc push             # Upload tracked files or directories to remote storage.
dvc status           # Show changed stages, compare local cache and a remote storage.
dvc checkout         # Checkout data files from cache (use after git checkout).
dvc fetch            # Download files or directories from remote storage **to the cache**.
dvc cache            # Manage cache settings.
dvc repro            # Reproduce complete or partial pipelines by executing their stages.

dvc du               # Show disk usage.
dvc check-ignore     # Check whether files or directories are excluded due to `.dvcignore`.
dvc config           # Get or set config options.
dvc dag              # Visualize DVC project DAG.
dvc destroy          # Remove DVC files, local DVC config and data cache.
dvc diff             # Show added, modified, or deleted data between commits in the DVC repository, or between a commit and the workspace.
dvc root             # Return the relative path to the root of the DVC project.

dvc move (mv)        # Rename or move a DVC controlled data file or a directory.
dvc remove (rm)      # Remove stages from dvc.yaml and/or stop tracking files or directories.

### Download commands
dvc get              # Download file or directory tracked by DVC or by Git.
dvc get-url          # Download or copy files from URL.
dvc import           # Download file or directory tracked by DVC or by Git into the workspace, and track it.
dvc import-db        # Snapshot a table or a SQL query result to a CSV/JSON format
dvc import-url       # Download or copy file from URL and take it under DVC control.
dvc update           # Update data artifact imported (via dvc import or dvc import-url) from an external DVC repository or URL.

## Install DVC git hooks into the repository.
dvc install

## List
dvc list (ls)           # List repository contents, including files and directories tracked by DVC and by Git.
dvc list-url (ls-url)   # List directory contents from URL.


## ====================================== Set up and manage data remotes ====================================== ##
dvc remote add                 # Add a new data remote.
dvc remote default             # Set/unset the default data remote.
dvc remote modify              # Modify the configuration of a data remote.
dvc remote list                # List all available data remotes.
dvc remote remove              # Remove a data remote.
dvc remote rename              # Rename a DVC remote

## ====================================== Commands related to data management ====================================== ##
dvc data

## ====================================== Commands to run and compare experiments ====================================== ##
dvc experiments (exp)

## ====================================== DVC model registry artifact commands ====================================== ##
dvc artifacts

## ====================================== Commands to list and create stages ====================================== ##
dvc stage

# To enable auto staging, run:
dvc config core.autostage true

dvc freeze           # Freeze stages or .dvc files.
dvc unfreeze         # Unfreeze stages or .dvc files.

## ====================================== Commands to display and compare metrics ====================================== ##
dvc metrics show
dvc metrics show

## ====================================== Commands to display params ====================================== ##
dvc params diff

## ====================================== Commands to visualize and compare plot data ====================================== ##
dvc plots show

## ====================================== Commands to manage experiments queue ====================================== ##
dvc queue


## ====================================== Not too important ====================================== ##
dvc completion       # Generate shell tab completion.
dvc gc               # Garbage collect unused objects from cache or remote storage.
dvc studio           # Commands to authenticate DVC with Iterative Studio
dvc unprotect        # Unprotect tracked files or directories (when hardlinks or symlinks have been enabled with `dvc config cache.type`).


## options:
--wait-for-lock    # Wait for the lock if it is already held by another process, instead of failing immediately.
```
