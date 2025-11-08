package com.example.myandroidapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class GradeCalculatorActivity : AppCompatActivity() {

    private lateinit var grade1EditText: EditText
    private lateinit var grade2EditText: EditText
    private lateinit var grade3EditText: EditText
    private lateinit var calculateButton: Button
    private lateinit var resultTextView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_grade_calculator)

        grade1EditText = findViewById(R.id.grade1EditText)
        grade2EditText = findViewById(R.id.grade2EditText)
        grade3EditText = findViewById(R.id.grade3EditText)
        calculateButton = findViewById(R.id.calculateButton)
        resultTextView = findViewById(R.id.resultTextView)

        calculateButton.setOnClickListener {
            calculateAverage()
        }
    }

    private fun calculateAverage() {
        val grade1 = grade1EditText.text.toString().toFloatOrNull()
        val grade2 = grade2EditText.text.toString().toFloatOrNull()
        val grade3 = grade3EditText.text.toString().toFloatOrNull()

        if (grade1 != null && grade2 != null && grade3 != null) {
            val average = (grade1 + grade2 + grade3) / 3
            val result = if (average >= 6) "Approved" else "Failed"
            resultTextView.text = "Average: $average\nResult: $result"
        } else {
            resultTextView.text = "Please enter valid grades."
        }
    }
}