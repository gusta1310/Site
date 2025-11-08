package com.example.myandroidapp

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnBmiCalculator.setOnClickListener {
            val intent = Intent(this, BmiCalculatorActivity::class.java)
            startActivity(intent)
        }

        btnGradeCalculator.setOnClickListener {
            val intent = Intent(this, GradeCalculatorActivity::class.java)
            startActivity(intent)
        }

        btnAboutDeveloper.setOnClickListener {
            val intent = Intent(this, AboutDeveloperActivity::class.java)
            startActivity(intent)
        }
    }
}