# Flutter

Flutter is an open-source UI software development toolkit created by Google for developing natively compiled applications for mobile, web, and desktop from a single codebase. The key features of Flutter include:

- **Fast Development:** Flutter's hot reload helps you quickly and easily experiment, build UIs, add features, and fix bugs faster.
- **Expressive and Flexible UI:** Flutter includes a rich set of fully customizable widgets to build native interfaces in minutes.
- **Native Performance:** Flutter’s widgets incorporate all critical platform differences such as scrolling, navigation, icons, and fonts to provide full native performance on both iOS and Android.

## Getting Started on Linux

### Software Requirements

To install, write, and compile Flutter code, you need the following requirements:

- **Operating system**
   - Flutter supports Debian Linux 11 or later and Ubuntu Linux 20.04 LTS or later.

- **Development tools on Linux**

1. Verify that you have the following tools installed: `bash`, `file`, `mkdir`, `rm`, `which`

```shell
    which bash file mkdir rm which
    /bin/bash
    /usr/bin/file
    /bin/mkdir
    /bin/rm
    which: shell built-in command
```

2. Install the following packages: `curl`, `git`, `unzip`, `xz-utils`, `zip`, `libglu1-mesa`

```shell
    sudo apt-get update -y && sudo apt-get upgrade -y;
    sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa
```

3. Install Git (if you do not have it)

```shell
    sudo apt update
    sudo apt install git
```

4. Install Flutter for Linux

   - [Download Flutter for Linux](https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.2-stable.tar.xz)
   - Extract the file to your desired location.
   - Navigate to the `bin` folder in your command terminal.
   - Type `pwd` to view the path, then copy it.
   - Open a new tab in your command terminal, ensure you are in the home directory.
   - Type `gedit .bashrc` and press `Enter`.
   - Scroll to the bottom of the file and add `export PATH="$PATH:<paste your path here>"`.
   - To verify the path, restart your command terminal and type `which flutter`; you should see the Flutter path.

5. Install Android Studio

   - [Download Android Studio for Linux](https://developer.android.com/studio?gad_source=1&gclid=CjwKCAjwnK60BhA9EiwAmpHZwzcJ_XDHOxfhA-EcY_u9F_0i76qWNUdVy08wS5e4SdJ7o2HARry66RoCas4QAvD_BwE&gclsrc=aw.ds)
   - Extract the file to your desired location.
   - Navigate to the `bin` directory of your Android Studio in the command terminal.
   - Type `./studio.sh` and press `Enter`.
   - Follow the Android Studio setup to install the latest Android SDK, Android SDK platform tools, and Android SDK build tools.
   - After the download completes, open Android Studio, click on the `plugins` tab.
      - Search for `flutter` and install it.
      - Search for `Dart` and install it.
      - Once installed, click `Restart Android Studio`.
      - After Android Studio restarts, you should see the `Start a new Flutter project` button on the welcome page, indicating successful installation.
   - To create a Flutter project:
      - Click on `Create new Flutter Project`.
      - Select `Flutter`.
      - Enter the path to your Flutter Directory.
         - Example:
         - `/home/usr/flutter`
      - Enter the project name and click `Create`.

6. Example Code

```dart
    import 'package:flutter/material.dart';

    void main() {
      runApp(const MyApp());
    }

    class MyApp extends StatelessWidget {
      const MyApp({Key? key});

      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            colorScheme: ColorScheme.fromSwatch(primarySwatch: Colors.deepPurple),
            // more theme settings...
          ),
          home: const MyHomePage(title: 'Flutter Demo Home Page'),
        );
      }
    }

    class MyHomePage extends StatefulWidget {
      const MyHomePage({Key? key, required this.title});

      @override
      _MyHomePageState createState() => _MyHomePageState();
    }

    class _MyHomePageState extends State<MyHomePage> {
      int _counter = 0;

      void _incrementCounter() {
        setState(() {
          _counter++;
        });
      }

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            backgroundColor: Theme.of(context).colorScheme.secondary,
            title: Text(widget.title),
          ),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                const Text(
                  'You have pushed the button this many times:',
                ),
                Text(
                  '$_counter',
                  style: Theme.of(context).textTheme.headline6,
                ),
              ],
            ),
          ),
          floatingActionButton: FloatingActionButton(
            onPressed: _incrementCounter,
            tooltip: 'Increment',
            child: const Icon(Icons.add),
          ),
        );
      }
    }
```

- Once you are ready to test the code:
      - Click on the `Device Manager` tab on the right of your Android Studio window.
      - Click on the `+` sign to choose `Create Virtual Device`.
      - Select your desired hardware and download the necessary system image.
