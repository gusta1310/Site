# MyAndroidApp

MyAndroidApp is an Android application developed in Kotlin that features four main screens: a main screen with navigation buttons, a BMI calculator, a grade calculator, and an about developer screen.

## Features

- **Main Screen**: The entry point of the application with navigation buttons to access other functionalities.
- **BMI Calculator**: Allows users to input their weight and height to calculate their Body Mass Index (BMI).
- **Grade Calculator**: Users can input three grades to calculate the average and determine if they pass or fail.
- **About Developer**: Displays information about the developer, including their name, RGM, and a photo.

## Project Structure

```
MyAndroidApp
├── app
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── com
│   │   │   │       └── example
│   │   │   │           └── myandroidapp
│   │   │   │               ├── MainActivity.kt
│   │   │   │               ├── BmiCalculatorActivity.kt
│   │   │   │               ├── GradeCalculatorActivity.kt
│   │   │   │               └── AboutDeveloperActivity.kt
│   │   │   └── res
│   │   │       ├── layout
│   │   │       │   ├── activity_main.xml
│   │   │       │   ├── activity_bmi_calculator.xml
│   │   │       │   ├── activity_grade_calculator.xml
│   │   │       │   └── activity_about_developer.xml
│   │   │       └── values
│   │   │           ├── strings.xml
│   │   │           └── colors.xml
├── build.gradle
└── README.md
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Open the project in Android Studio.
3. Ensure that you have the necessary SDKs installed (compileSdkVersion 31).
4. Build and run the application on an Android device or emulator.

## Usage

- Launch the application to access the main screen.
- Use the navigation buttons to switch between the BMI calculator, grade calculator, and about developer screens.
- Follow the prompts on each screen to input data and view results.

## License

This project is open-source and available for modification and distribution.