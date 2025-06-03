# Android App Development Setup Notes

This file documents the steps to scaffold and configure the Android app project, with a focus on a streamlined, working setup for Kotlin and Jetpack Compose.

---

## What is Gradle?
Gradle is a build automation tool used for Java and Android projects. It manages dependencies, compiles code, and packages applications. Android Studio uses Gradle as its default build system.

### Why Gradle?
- Automates the build process
- Manages dependencies (libraries and frameworks)
- Allows customization of the build process

---

## Setup Steps

### 1. Install Gradle (Initial Attempt)
```bash
sudo apt update && sudo apt install gradle -y
```
- Installs Gradle from the system package manager (often outdated).

### 2. Initialize the Android Project
```bash
cd /home/ubuntu/projects/curioswipe/mobile && gradle init --type basic
```
- Sets up a basic Gradle project structure.

### 3. Initialize for Kotlin
```bash
cd /home/ubuntu/projects/curioswipe/mobile && gradle init --type kotlin-application
```
- Adds Kotlin-specific project structure and sample code.

### 4. Create Main.kt (Kotlin Hello World)
```bash
cd /home/ubuntu/projects/curioswipe/mobile/src/main/kotlin && touch Main.kt
```
- Simple entry point for Kotlin, to verify the toolchain.

**Main.kt**:
```kotlin
package main.kotlin

fun main() {
    println("Hello, Kotlin Android App!")
}
```

---

### 5. Install SDKMAN and Latest Kotlin
```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install kotlin
```
- Ensures the latest Kotlin version is installed and available.

---

### 6. Verify Kotlin Setup
```bash
cd /home/ubuntu/projects/curioswipe/mobile/src/main/kotlin
kotlinc Main.kt -include-runtime -d Main.jar
java -jar Main.jar
```
- Output should be:
  ```
  Hello, Kotlin Android App!
  ```
- Confirms Kotlin is working.

---

### 7. Gradle/Java Compatibility Issue & Solution

#### Problem
- Gradle build failed with:
  > Could not determine java version from '11.0.27'.
- Cause: System Gradle version (4.4.1) was too old for Java 11.

#### Solution
1. Verified Gradle version (`gradle --version`): 4.4.1 (too old for Java 11).
2. Upgraded Gradle Wrapper to 7.6.4 by editing `gradle-wrapper.properties`:
   - `distributionUrl=https\://services.gradle.org/distributions/gradle-7.6.4-bin.zip`
3. Ran `./gradlew --version` to confirm upgrade.
4. Restructured project:
   - Created a top-level `build.gradle` for plugin classpaths and repositories.
   - Moved app configuration to `app/build.gradle` (with only `plugins`, `android`, `dependencies`, and `repositories` blocks).
   - Updated `settings.gradle` to include `:app` module.
5. Ran `./gradlew build` successfully (no plugin errors).

#### Current Structure
- `mobile/build.gradle` (top-level, configures plugins and repositories)
- `mobile/app/build.gradle` (app module, contains Android app config)
- `mobile/settings.gradle` (includes `:app`)

---

## Next Steps
1. Implement Android app features using Kotlin and Jetpack Compose.
2. Start with a basic UI for swipeable topics in `MainActivity.kt`.
3. Test the app to ensure all dependencies and configurations work.

---

**All Gradle/Java compatibility issues are now resolved. You can proceed with Android app development.**
