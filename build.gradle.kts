plugins {
    kotlin("jvm") version "1.6.10"
}

// build-system dependencies
buildscript {
    repositories {
        mavenCentral()
        google()
    }

    dependencies {
        // Android build
        classpath("com.android.tools.build:gradle:7.3.1")
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.7.22")
    }
}

// setup modules
allprojects {
    repositories {
        mavenCentral()
        google()

        // Logger
        maven(url = "https://jitpack.io")
    }

    tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
        kotlinOptions {
            freeCompilerArgs = listOf("-Xjsr305=strict")
            jvmTarget = "1.8"
        }
    }
}
