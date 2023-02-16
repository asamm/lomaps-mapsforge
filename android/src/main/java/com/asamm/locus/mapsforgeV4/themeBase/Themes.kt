package com.asamm.locus.mapsforgeV4.themeBase

import org.mapsforge.map.rendertheme.XmlRenderTheme
import org.mapsforge.map.rendertheme.XmlRenderThemeMenuCallback
import org.mapsforge.map.rendertheme.XmlThemeResourceProvider
import java.io.InputStream

object Themes {

    // default prefix/path for internal themes
    const val DEFAULT_PREFIX = "themes/mapsforgeV4/base/"

    // base of the file name
    const val BASE_THEME_NAME = "theme"

    val themeCar: XmlRenderTheme
        get() = InternalRenderTheme(DEFAULT_PREFIX, BASE_THEME_NAME, "car")

    val themeCity: XmlRenderTheme
        get() = InternalRenderTheme(DEFAULT_PREFIX, BASE_THEME_NAME, "city")

    val themeHikeBike: XmlRenderTheme
        get() = InternalRenderTheme(DEFAULT_PREFIX, BASE_THEME_NAME, "hike_bike")

    val themeSki: XmlRenderTheme
        get() = InternalRenderTheme(DEFAULT_PREFIX, BASE_THEME_NAME, "ski")

    /**
     * Internal theme included in Locus application.
     *
     * @param pathPrefix prefix for map path
     * @param name name of theme
     * @param type type of theme
     */
    class InternalRenderTheme(
        private val pathPrefix: String,
        private val name: String,
        val type: String
    ) : XmlRenderTheme {

        private var menuCallback: XmlRenderThemeMenuCallback? = null

        override fun getRelativePathPrefix(): String {
            return pathPrefix
        }

        override fun getRenderThemeAsStream(): InputStream {
            return Themes::class.java.getResourceAsStream("/assets/$pathPrefix$name.xml")!!
        }

        override fun getMenuCallback(): XmlRenderThemeMenuCallback? {
            return menuCallback
        }

        override fun setMenuCallback(xmlRenderThemeMenuCallback: XmlRenderThemeMenuCallback) {
            menuCallback = xmlRenderThemeMenuCallback
        }

        override fun getResourceProvider(): XmlThemeResourceProvider? {
            return null
        }

        override fun setResourceProvider(xmlThemeResourceProvider: XmlThemeResourceProvider) {}
    }
}
