# Nexus Lab1: Nexus Installation and WebUI Usage

Date: Nov 6 2025

Written by: Kevin Li

## Step 1: Run the Nexus Docker Instance

1. Create a folder called `nexus-data` in your current working directory.

   > Note: in the command below, `nexus-data` is a Docker **named volume**, and Docker creates it for you.
   > A folder on disk is only needed if you switch to a bind mount (for example
   > `-v $(pwd)/nexus-data:/nexus-data`), in which case the folder must be writable by the user inside the container.

2. Start the container:

```bash
docker run -d -p 8081:8081 --name nexus \
  -v nexus-data:/nexus-data \
  sonatype/nexus3
```

   The image `sonatype/nexus3` comes from Docker Hub: [https://hub.docker.com/r/sonatype/nexus3](https://hub.docker.com/r/sonatype/nexus3)

3. Follow the container logs:

```bash
docker logs -f 3cedcd8a1a28e153695bfd553cc37c4464f73b2912ea5af9218b8a59b91eba9c &
```

Explanation:

* The hash id `3cedcd8a1a28e153695bfd553cc37c4464f73b2912ea5af9218b8a59b91eba9c` is the container id from
  the author's machine. Please replace it with your own container id (or simply use the container name,
  `docker logs -f nexus &`) and do not use this one.
* `&` at the end releases the terminal back to you, as the command runs as a background job.
* `-f` outputs the log in real time (follow mode).

![docker logs -f output](../../../../../images/dev_ops/nexus/nexus_webui_logs_follow.png)

At the bottom, if you hit Enter, you get your terminal back. The terminal is not stuck, since the
`docker logs -f ...` process is running in the background.

![Hit Enter to get the terminal prompt back](../../../../../images/dev_ops/nexus/nexus_webui_logs_prompt.png)

Now in the log window, scroll up and you should see a line like the one below.

![Started Sonatype Nexus COMMUNITY 3.86.0-08](../../../../../images/dev_ops/nexus/nexus_webui_logs_started.png)

It shows the version, and that the Nexus instance has started successfully.

## Step 2: Get the Password and Log In

Next, let us get the initial admin password.

```bash
docker exec -it nexus cat /nexus-data/admin.password
```

![Output of docker exec showing the admin password](../../../../../images/dev_ops/nexus/nexus_webui_admin_password.png)

Go to your browser and open this URL:

```text
localhost:8081
```

For the author, the password was `83952577-6b16-42ec-ac03-43f711834b48`.

> Note: for you, the password will be different. If the command says `No such file or directory`,
> see **Troubleshooting: admin.password Not Found** below.

Log in as `admin` with that password. A setup wizard then starts. Change the password for the first time.

![Wizard 1 of 6: Welcome](../../../../../images/dev_ops/nexus/nexus_webui_wizard_1_welcome.png)

![Wizard 2 of 6: Choose a password for the admin user](../../../../../images/dev_ops/nexus/nexus_webui_wizard_2_password.png)

Next screens:

![Wizard 3 of 6: Discover Community Edition](../../../../../images/dev_ops/nexus/nexus_webui_wizard_3_community.png)

![Wizard 4 of 6: Agree End User License Agreement](../../../../../images/dev_ops/nexus/nexus_webui_wizard_4_eula.png)

Select the first option. As of now, we choose **Enable anonymous access**.

![Wizard 5 of 6: Configure Anonymous Access](../../../../../images/dev_ops/nexus/nexus_webui_wizard_5_anonymous.png)

![Wizard 5 of 6: Enable anonymous access selected](../../../../../images/dev_ops/nexus/nexus_webui_wizard_5_anonymous_enabled.png)

For our future labs we will just work with this option.

![Wizard 6 of 6: Setup Complete](../../../../../images/dev_ops/nexus/nexus_webui_wizard_6_complete.png)

## Step 3: Upload an Artifact

First, click on **Browse**.

![Dashboard](../../../../../images/dev_ops/nexus/nexus_webui_dashboard.png)

![Browse repositories](../../../../../images/dev_ops/nexus/nexus_webui_browse.png)

Then click on `maven-central`.

![Click maven-central](../../../../../images/dev_ops/nexus/nexus_webui_browse_maven_central.png)

Remember [https://mvnrepository.com/](https://mvnrepository.com/)? That is similar to this.

Then let us go to **Upload** to upload an artifact.

![Upload: hosted repositories](../../../../../images/dev_ops/nexus/nexus_webui_upload_repos.png)

Click on `maven-releases`, and you will see the following screen.

![Select maven-releases](../../../../../images/dev_ops/nexus/nexus_webui_upload_select_maven_releases.png)

![Upload form for the maven-releases repository](../../../../../images/dev_ops/nexus/nexus_webui_upload_form.png)

Pick a jar you built (here, `spring-boot-complete-0.0.1-SNAPSHOT.jar`).

![Choose File dialog](../../../../../images/dev_ops/nexus/nexus_webui_upload_choose_file.png)

You will see that the jar is selected and the **Extension** field is filled in (`jar`).

![File selected, Extension is jar](../../../../../images/dev_ops/nexus/nexus_webui_upload_file_selected.png)

For the component coordinates, fill in the **Group ID**, **Artifact ID** and **Version** fields (in this
lab: `abc`, `abc.def` and `1.0`), then upload.

![Component coordinates](../../../../../images/dev_ops/nexus/nexus_webui_upload_coordinates.png)

After uploading, you will see "The form was saved successfully", and the component in the search results.
Click on the component.

![Upload saved and search results](../../../../../images/dev_ops/nexus/nexus_webui_upload_saved.png)

This is how the component looks. Click on the jar asset.

![Component details and assets](../../../../../images/dev_ops/nexus/nexus_webui_component_details.png)

The asset **Summary** tab shows the path, content type, file size and uploader.

![Asset summary](../../../../../images/dev_ops/nexus/nexus_webui_asset_summary.png)

The **Usage** tab shows the snippet to insert into your `pom.xml` to use this artifact as a Maven dependency.

![Asset usage snippet for Apache Maven](../../../../../images/dev_ops/nexus/nexus_webui_asset_usage.png)

## Troubleshooting: admin.password Not Found

If `docker exec -it nexus cat /nexus-data/admin.password` returns `No such file or directory`,
work through these in order.

### 1. Nexus may still be starting

Nexus can take 1-2 minutes to initialize on first boot. Tail the logs and wait for the
"Started Sonatype Nexus" line before retrying:

```bash
docker logs -f nexus
```

### 2. Check folder/volume permissions

The Nexus process inside the container runs as UID `200`. If `/nexus-data` is not writable by
that user, Nexus fails to create `admin.password` (and may fail to start at all). Check the
mount's ownership:

```bash
docker exec -it nexus ls -la /nexus-data
```

* If you used the **named volume** from Step 1 (`-v nexus-data:/nexus-data`), Docker manages
  the permissions for you, so this is rarely the cause.
* If you used a **bind mount** to a host folder instead (e.g. `-v $(pwd)/nexus-data:/nexus-data`),
  fix the ownership on the host so UID `200` can write to it:

```bash
sudo chown -R 200:200 ./nexus-data
docker restart nexus
```

* On Linux, also make sure no overly restrictive permission bits are blocking access
  (`chmod -R u+rwX ./nexus-data` after the `chown`, if needed).

### 3. The password file is gone for a legitimate reason

* **Already changed:** Nexus deletes `admin.password` the first time you log in and set a new
  password through the setup wizard. If you already completed Step 2 once, there's no password
  file to find anymore — use the password you set instead.
* **Reused an old volume:** if `nexus-data` was created by a previous Nexus container (or a
  previous run of this lab), it already has an admin account and no fresh `admin.password`.

### 4. Delete the Docker volume and start fresh

If the checks above don't resolve it, the simplest fix is to wipe the container and its volume
and repeat Step 1 from scratch. This deletes all Nexus data (repositories, uploaded
components, settings), so only do this in a lab/dev environment.

```bash
# Stop and remove the container
docker rm -f nexus

# List volumes if you're not sure of the exact name
docker volume ls

# Remove the named volume used in Step 1
docker volume rm nexus-data

# Recreate and start fresh (Step 1 again)
docker run -d -p 8081:8081 --name nexus \
  -v nexus-data:/nexus-data \
  sonatype/nexus3
```

Then tail the logs again and retry `docker exec -it nexus cat /nexus-data/admin.password` once
you see `Started Sonatype Nexus` in the output.

