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

## dvc.yaml
- It's like a pipeline file.
- Has a `dvc.lock` state like terraform, it's a replacement for the `data.csv.dvc` file.
>dvc repro
- You can push content of `outs` files to the remote:
>dvc push

## Pull data or Pipeline steps
>dvc pull