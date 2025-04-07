# Introduction

This repo is intended to show a ci for an ml model. It was created when following certain video on datacamps course CI/CD for machine learning.

Create a branch adjust something small (e.g. the README.md), commit the change and merge the branch into the main branch. 

This should trigger a github action that trains a model to check if all is ok. Metrics are written to the comments track of the pull request. Then you can close the pull request and delete the branch.

## DVC - data versioning

create dvc repo
`dvc init`

add a file 
`dvc add <filename>`

setting up remote repo's 
`dvc remote add -d myAWSremote s3://mybucket`

setting up local and default remotes:
`dvc remote add mylocalremote /tmp/dvc`

use the `-d` flag to set the default repo.
`dvc remote add -d mylocalremote /tmp/dvc`

uploading and retrieving data
`dvc push <target>`

`dvc pull <target>`

`dvc push` if you have set a default repo. 

to see the remotes
`dvc remote list`

## DVC - pipelines

generate a pipelines with `dvc stage add`. This saves the stage in the `dvc.yaml`. 

`dvc repro` to run the the pipeline

`dvc dag` to visualize the result.

aag changes
