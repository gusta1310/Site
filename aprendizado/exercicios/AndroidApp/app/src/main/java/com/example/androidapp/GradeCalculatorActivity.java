package com.example.androidapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class GradeCalculatorActivity extends AppCompatActivity {

    private EditText grade1Input;
    private EditText grade2Input;
    private EditText grade3Input;
    private Button calculateButton;
    private TextView resultTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_grade_calculator);

        grade1Input = findViewById(R.id.grade1Input);
        grade2Input = findViewById(R.id.grade2Input);
        grade3Input = findViewById(R.id.grade3Input);
        calculateButton = findViewById(R.id.calculateButton);
        resultTextView = findViewById(R.id.resultTextView);

        calculateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateAverage();
            }
        });
    }

    private void calculateAverage() {
        String grade1Str = grade1Input.getText().toString();
        String grade2Str = grade2Input.getText().toString();
        String grade3Str = grade3Input.getText().toString();

        if (!grade1Str.isEmpty() && !grade2Str.isEmpty() && !grade3Str.isEmpty()) {
            double grade1 = Double.parseDouble(grade1Str);
            double grade2 = Double.parseDouble(grade2Str);
            double grade3 = Double.parseDouble(grade3Str);

            double average = (grade1 + grade2 + grade3) / 3;
            String result;

            if (average >= 6) {
                result = "Aprovado! Média: " + average;
            } else {
                result = "Reprovado! Média: " + average;
            }

            resultTextView.setText(result);
        } else {
            resultTextView.setText("Por favor, preencha todas as notas.");
        }
    }
}