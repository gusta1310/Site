package com.example.myandroidapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class BmiCalculatorActivity : AppCompatActivity() {

    private lateinit var weightEditText: EditText
    private lateinit var heightEditText: EditText
    private lateinit var calculateButton: Button
    private lateinit var resultTextView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_bmi_calculator)

        weightEditText = findViewById(R.id.weightEditText)
        heightEditText = findViewById(R.id.heightEditText)
        calculateButton = findViewById(R.id.calculateButton)
        resultTextView = findViewById(R.id.resultTextView)

        calculateButton.setOnClickListener {
            calculateBMI()
        }
    }

    private fun calculateBMI() {
        val weight = weightEditText.text.toString().toFloatOrNull()
        val height = heightEditText.text.toString().toFloatOrNull()

        if (weight != null && height != null && height > 0) {
            val bmi = weight / (height * height)
            resultTextView.text = String.format("Your BMI is: %.2f", bmi)
        } else {
            resultTextView.text = "Please enter valid weight and height."
        }
    }
}