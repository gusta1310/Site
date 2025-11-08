package com.example.myandroidapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_about_developer.*

class AboutDeveloperActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_about_developer)

        // Set developer information
        val developerName = "Your Name"
        val developerRGM = "Your RGM"
        val developerPhoto = R.drawable.developer_photo // Ensure you have a drawable resource named developer_photo

        nameTextView.text = developerName
        rgmTextView.text = developerRGM
        developerImageView.setImageResource(developerPhoto)
    }
}