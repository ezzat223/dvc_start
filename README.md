## Commands
- Initialize DVC:
>dvc init

- Add the data file (use it each time there're changes just like the git add . command):
>dvc add data/data.csv # <path-to-the-.csv>

- To enable auto staging, run:
>dvc config core.autostage true

- Bring data of version of current md5:
>dvc checkout 
- Use case of this is when you git checkout to a certain commit then use dvc checkout to bring the version of data that was used with it.
- To make it happen automatically on git checkout without using dvc checkout command use this command which will add git hooks like pre and post commit:
>dvc install


- Remote repo (eg: local-file, s3-bucket...):
>dvc remote add -d <remote-name> <remote-url-or-path>

- Moves a tracked file or directory to a new location while keeping the history:
>dvc move <old_path> <new_path>

## dvc.yaml Pipeline
- Has a `dvc.lock` state like terraform, it's a replacement for the `data.csv.dvc` file.
- Reproduces the pipeline (steps) based on changes to dependencies.
>dvc repro

- Reproduce a specific stage:
>dvc repro <stage-name>

- Runs an experiment, potentially with parameter or config changes:
>dvc exp run -S param1=100 -S param2=0.1


- You can push content of `outs` files to the remote:
>dvc push

- Shows changes in parameters used by your pipeline stages.
>dvc params diff

- Shows the latest metrics from a project (requires metrics files to be defined in DVC files):
>dvc metrics show

- Generates and displays plots from the tracked metrics:
>dvc plots show

## Pull data or Pipeline steps
- pulls the data and places it in the cwd But doesn't track it
>dvc pull

- pulls the data and places it in the cwd and keeps on tracking it
>dvc import

- pulls the data but doesn't places it in the cwd or track it
>dvc fetch



- Lists files and directories in a remote or a DVC repository:
>dvc list <url_or_path>

- Checks the DVC environment and reports any potential issues:
>dvc doctor