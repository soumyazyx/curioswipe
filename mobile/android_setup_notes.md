# Android App Development Setup Notes

This file documents all the steps taken to scaffold the Android app project, along with detailed explanations for each command and concept.

---

## **What is Gradle?**
Gradle is a build automation tool used primarily for Java and Android projects. It helps manage dependencies, compile code, and package applications. Android Studio uses Gradle as its default build system.

### **Why Did We Install Gradle?**
Gradle is essential for Android development because:
- It automates the build process.
- It manages dependencies (libraries and frameworks).
- It allows customization of the build process.

Since Gradle was not installed on the system, we installed it to scaffold the Android app project.

---

## **Commands Run**

### **1. Install Gradle**
```bash
sudo apt update && sudo apt install gradle -y
```
- **Purpose**: Install Gradle on the system.
- **Explanation**: Gradle is required to initialize and build Android projects.

### **2. Initialize the Android Project**
```bash
cd /home/ubuntu/projects/curioswipe/mobile && gradle init --type basic
```
- **Purpose**: Create a basic Gradle project in the `mobile` folder.
- **Explanation**: This command sets up the initial project structure, including files like `build.gradle` and `settings.gradle`.

### **3. Initialize the Android Project for Kotlin**
```bash
cd /home/ubuntu/projects/curioswipe/mobile && gradle init --type kotlin-application
```
- **Purpose**: Scaffold the Android app with Kotlin-specific configurations.
- **Explanation**: This command sets up the project structure optimized for Kotlin development, including source directories and a sample `Main` class.

### **4. Create Main.kt File**
```bash
cd /home/ubuntu/projects/curioswipe/mobile/src/main/kotlin && touch Main.kt
```
- **Purpose**: This file serves as the entry point for the Kotlin application.
- **Explanation**: While Android apps typically use an `Activity` as the entry point, this file is a basic starting point for Kotlin development. It contains a simple `main` function that prints "Hello, Kotlin Android App!" to the console.

**Contents of Main.kt**:
```kotlin
package main.kotlin

fun main() {
    println("Hello, Kotlin Android App!")
}
```
- **Why**: Helps you understand Kotlin basics and serves as a placeholder for future Android-specific code.

---

### **5. Update build.gradle File**
```bash
nano /home/ubuntu/projects/curioswipe/mobile/build.gradle
```
- **Purpose**: Configure the project for Android development using Kotlin and Jetpack Compose.
- **Explanation**: Added Android-specific configurations and dependencies to the `build.gradle` file.

**Key Changes**:
- **Plugins**:
  - Added `com.android.application` for Android app development.
  - Added `org.jetbrains.kotlin.android` for Kotlin support.
- **Android Configuration**:
  - Set `compileSdkVersion` to 33 (latest SDK version).
  - Defined `minSdkVersion` (21) and `targetSdkVersion` (33) for compatibility.
  - Configured `applicationId` as `"com.example.curioswipe"`.
- **Dependencies**:
  - Added libraries for Android development, including:
    - **Jetpack Compose**: For building modern UI.
    - **Kotlin Standard Library**: Core Kotlin functionality.
    - **AndroidX Libraries**: For compatibility and lifecycle management.
    - **Material Design**: For UI components.
    - **Navigation Compose**: For handling navigation in the app.
    - **Testing Libraries**: For unit and UI testing.

**Updated build.gradle Contents**:
```gradle
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    compileSdkVersion 33

    defaultConfig {
        applicationId "com.example.curioswipe"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib:1.8.0"
    implementation "androidx.core:core-ktx:1.9.0"
    implementation "androidx.appcompat:appcompat:1.6.1"
    implementation "com.google.android.material:material:1.8.0"
    implementation "androidx.constraintlayout:constraintlayout:2.1.4"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.5.1"
    implementation "androidx.activity:activity-compose:1.6.1"
    implementation "androidx.compose.ui:ui:1.3.1"
    implementation "androidx.compose.material:material:1.3.1"
    implementation "androidx.compose.ui:ui-tooling-preview:1.3.1"
    implementation "androidx.navigation:navigation-compose:2.5.3"
    testImplementation "junit:junit:4.13.2"
    androidTestImplementation "androidx.test.ext:junit:1.1.5"
    androidTestImplementation "androidx.test.espresso:espresso-core:3.5.1"
    androidTestImplementation "androidx.compose.ui:ui-test-junit4:1.3.1"
    debugImplementation "androidx.compose.ui:ui-tooling:1.3.1"
}
```

---

## **Project Structure Created**
After running the `gradle init` command, the following files and folders were created:

- **`build.gradle`**: The main build configuration file.
- **`settings.gradle`**: Specifies project settings.
- **`gradlew` and `gradlew.bat`**: Gradle wrapper scripts for Linux and Windows.
- **`gradle/wrapper/`**: Contains Gradle wrapper files.
  - `gradle-wrapper.jar`: The Gradle wrapper executable.
  - `gradle-wrapper.properties`: Configuration for the Gradle wrapper.

---

## **Updated Project Structure Created**
After running the `gradle init --type kotlin-application` command, the following files and folders were created:

- **`src/main/kotlin/`**: Directory for Kotlin source files.
- **`src/test/kotlin/`**: Directory for Kotlin test files.
- **`build.gradle.kts`**: Kotlin DSL build configuration file.
- **`settings.gradle.kts`**: Specifies project settings using Kotlin DSL.
- **`gradlew` and `gradlew.bat`**: Gradle wrapper scripts for Linux and Windows.
- **`gradle/wrapper/`**: Contains Gradle wrapper files.
  - `gradle-wrapper.jar`: The Gradle wrapper executable.
  - `gradle-wrapper.properties`: Configuration for the Gradle wrapper.

---

### **6. Install SDKMAN and Kotlin**
```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install kotlin
```
- **Purpose**: Install SDKMAN, a tool for managing development kits, and use it to install Kotlin.
- **Explanation**:
  - SDKMAN simplifies the installation and management of software development kits.
  - Kotlin was installed using SDKMAN, ensuring the latest version is set up.

**Steps Taken**:
1. Installed SDKMAN by running the `curl` command.
2. Initialized SDKMAN using the `source` command.
3. Installed Kotlin using the `sdk install kotlin` command.

**Verification**:
- After installation, Kotlin version 2.1.21 was set as the default.
- Verified the installation by running:
  ```bash
  kotlin -version
  ```

---

### **7. Run Main.kt File**
```bash
cd /home/ubuntu/projects/curioswipe/mobile/src/main/kotlin
kotlinc Main.kt -include-runtime -d Main.jar
java -jar Main.jar
```
- **Purpose**: Compile and execute the `Main.kt` file to verify the Kotlin setup.
- **Explanation**:
  - The `kotlinc` command compiles the Kotlin file into a JAR.
  - The `java -jar` command runs the compiled JAR file.

**Output**:
```
Hello, Kotlin Android App!
```
- **Why**: This confirms that the Kotlin setup is working correctly and the project is configured properly.

---

### **8. Current Status and Issue with Gradle**

- **Kotlin is successfully installed and verified** by compiling and running a simple `Main.kt` file.
- **Android app structure has been started** with a `MainActivity.kt` using Jetpack Compose for a basic UI.
- **OpenJDK 11 is installed and JAVA_HOME is set** to `/usr/lib/jvm/java-11-openjdk-arm64`.
- **Gradle build fails** with the error:
  > Could not determine java version from '11.0.27'.
- This error suggests a compatibility issue between the installed Gradle version and Java 11.



---

## Gradle/Java Compatibility Issue Resolved (June 2025)

### Problem
- Gradle build failed with:
  > Could not determine java version from '11.0.27'.
- Cause: The system Gradle version (4.4.1) was too old for Java 11.

### Solution Steps
1. Verified Gradle version (`gradle --version`): 4.4.1 (too old for Java 11).
2. Upgraded Gradle Wrapper to 7.6.4 by editing `gradle-wrapper.properties`:
   - `distributionUrl=https\://services.gradle.org/distributions/gradle-7.6.4-bin.zip`
3. Ran `./gradlew --version` to confirm upgrade.
4. Fixed build script errors:
   - Created a top-level `build.gradle` with `buildscript` and `allprojects` blocks for plugin classpaths and repositories.
   - Moved the app configuration to `app/build.gradle` with only the `plugins`, `android`, `dependencies`, and `repositories` blocks.
   - Updated `settings.gradle` to include `:app` module.
5. Ran `./gradlew build` successfully (no plugin errors).

### Current Structure
- `mobile/build.gradle` (top-level, configures plugins and repositories)
- `mobile/app/build.gradle` (app module, contains Android app config)
- `mobile/settings.gradle` (includes `:app`)

---

## **Next Steps**
1. Implement the Android app features using Kotlin and Jetpack Compose.
2. Start with a basic UI for swipeable topics in `MainActivity.kt`.
3. Test the app to ensure all dependencies and configurations work.

---

**All Gradle/Java compatibility issues are now resolved. You can proceed with Android app development.**
