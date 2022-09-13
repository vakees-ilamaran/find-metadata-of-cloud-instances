# find-metadata-of-cloud-instances
Retrieves the metadata of the instances, VM, Machines

## Prerequisite
- [Create an EC2 Linux instance on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [SSH into the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

## Install the dependency modules
    
    pip3 install -r requirements.txt
    
## How to run
```
python get_meta_aws.py --find_key <KEY>
```
