# Android App

This project is an Android application that includes four main screens:

1. **Main Screen**: The entry point of the application featuring buttons with icons for navigation to other activities.
2. **BMI Calculator**: A screen that allows users to calculate their Body Mass Index (IMC) by entering their height and weight.
3. **Grade Calculator**: A screen for calculating the average of three school grades, providing a pass/fail status based on the average.
4. **Developer Information**: A screen that displays information about the developer, including their name, RGM, and a photo.

## Project Structure

The project is organized as follows:

```
AndroidApp
├── app
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── com
│   │   │   │       └── example
│   │   │   │           └── androidapp
│   │   │   │               ├── MainActivity.java
│   │   │   │               ├── BmiActivity.java
│   │   │   │               ├── GradeCalculatorActivity.java
│   │   │   │               └── DeveloperInfoActivity.java
│   │   │   ├── res
│   │   │   │   ├── drawable
│   │   │   │   ├── layout
│   │   │   │   │   ├── activity_main.xml
│   │   │   │   │   ├── activity_bmi.xml
│   │   │   │   │   ├── activity_grade_calculator.xml
│   │   │   │   │   └── activity_developer_info.xml
│   │   │   │   ├── mipmap
│   │   │   │   └── values
│   │   │   │       ├── colors.xml
│   │   │   │       ├── strings.xml
│   │   │   │       └── styles.xml
│   │   │   ├── AndroidManifest.xml
│   │   │   └── build.gradle
├── build.gradle
└── README.md
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Open the project in Android Studio.
3. Build the project to download the necessary dependencies.
4. Run the application on an emulator or physical device.

## Features

- **User-Friendly Interface**: The application is designed with a simple and intuitive interface for easy navigation.
- **BMI Calculation**: Users can quickly calculate their BMI and understand their health status.
- **Grade Calculation**: The app provides a straightforward way to calculate and assess academic performance.
- **Developer Info**: Users can learn more about the developer behind the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.