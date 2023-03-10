plugins {
    id("com.android.library")
    id("kotlin-android")
    id("maven-publish")
}

val androidVersion: String by project

android {
    compileSdk = 33
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    buildToolsVersion = "33.0.1"

    // define default parameters
    defaultConfig {
        minSdk = 21
        targetSdk = 31
    }
}

dependencies {
    // MapsForge API
    compileOnly("org.mapsforge:mapsforge-map-android:0.18.0")
}

publishing {
    publications {
        register<MavenPublication>("release") {
            groupId = "com.asamm.locus"
            artifactId = "mapsforge-v4-theme-base"
            version = androidVersion

            afterEvaluate {
                from(components["release"])
            }
        }
    }
}
