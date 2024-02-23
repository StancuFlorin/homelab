This is a simple container that is running `nginx` to server static files from `./static` folder.

For now, it is only used by the [backup](../backup/) script to create a static json with the details of the last rsync. At the end, the json file is used by the [homepage](../homepage/) dashboard (a simple GET request) to display the data in a widget.