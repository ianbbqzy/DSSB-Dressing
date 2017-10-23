## DSSB-Dressing

#### Resources
- [Meeting Notes](https://docs.google.com/spreadsheets/d/1efbMRaKTUslNaygWW0ClOrDtDmz-vBPUSCbdVV24Pdw/edit#gid=255759195)


#### Team members (In alphabetical order)
- Chelsea
- Ian
- Jerry
- Ryan
- Sachit
- Sameer


#### Google Cloud (subjected to changes)
Make sure you communicate with other team members before turning on and off the instances. Before you set up an account (you need a credit card), you can ask Ian to turn on and off the instances for you. The reason why we should use Google Cloud is that it gives us access to GPU's (in the future, we only have a dummy instance rn, but it should be good enough for most computing tasks). You are welcome to develop on your local machine, but it'd be nice if you could sync it on the instance and make sure it also runs smoothly on Google Cloud.

###### Resources
- [Google Cloud Tutorial](http://cs231n.github.io/gce-tutorial/)

To set up an account follow the google cloud tutorial. If you want to skip that for now, directly follow the steps below. Please only refer to the tutorial after you set up an account. Instead, follow the steps below. (AKA ignore everything after "Connect to Your Virtual Instance and Download the Assignment" on the website)

First, download the Google Cloud SDK that is appropriate for your platform from [here](https://cloud.google.com/sdk/docs/) and follow their installation instructions. Make sure you have run all the steps including step 4 and 5

```
#4
./google-cloud-sdk/install.sh

#5
./google-cloud-sdk/bin/gcloud init

```

After you run init, You will be prompted for a few configuration options.

Pick cloud project to use:`[#] skilled-curve-182502`

Do you want to configure Google Compute Engine:
`Y`

Engine zone: `[#] us-west1-b`

After step 5, you can run the following command to access the instance,

`./google-cloud-sdk/bin/gcloud compute ssh --zone=us-west1-b instance-2`

Now you can set up a git repo on your home directory as well as your local machine.

#### Getting started (Creds to Zane Christenson for the readme template)
To work on this repo, run the following commands
```
# clone a local copy
git clone https://github.com/ianbbqzy/DSSB-Dressing

# navigate into the repo
cd DSSB-Dressing

# create a new development branch
git checkout -b <feature_name_here>

```
Make your changes to the new branch and then
```
# See what files have been changed
git status

# add new/altered files
git add <changed_files_here>

# commit your changes
git commit -m "A message describing your changes."

# push your changes to the remote repo
git push origin head
```
Your changes will now appear on github as a new feature branch. Your teammates can review your changes and merge
it into master.

Remember to run `git pull origin master` frequently to get the latest changes.

#### Jupyter Notebook (On google cloud)

Run this script to setup the requirements we most likely will need for running CNN's. Extracted from Stanford c231n. We will modify the requirements later.
```
cd DSSB-Dressing
./setup_googlecloud.sh
```

From now on, run the following in the project directory before you begin deving

`source .env/bin/activate`

Next you need to install anaconda
```
~ianlee/Anaconda3-4.0.0-Linux-x86_64.sh

jupyter notebook --generate-config

source ~/.bashrc
```

open `~/.jupyter/jupyter_notebook_config.py` and append the following to the file
```
c = get_config()

c.NotebookApp.ip = '*'

c.NotebookApp.open_browser = False

c.NotebookApp.port = 7000
```

You can run the following command to open up jupyter
`jupyter-notebook --no-browser --port=7000`

After, you can run this to exit the venv.

`deactivate`

#### Jupyter Notebook on your machine

```
# if you don't have this already
sudo pip install virtualenv

# Create a virtual environment
virtualenv -p python3 .env     

# Activate the virtual environment             
source .env/bin/activate         

pip install -r requirements.txt  # Install dependencies

deactivate
```

Remember to source the virtualenv b4 you do anything
