package com.example.androidapp;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class DeveloperInfoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_developer_info);

        TextView nameTextView = findViewById(R.id.developer_name);
        TextView rgmTextView = findViewById(R.id.developer_rgm);
        ImageView photoImageView = findViewById(R.id.developer_photo);

        nameTextView.setText("Gustavo Henrique Dos Santos");
        rgmTextView.setText("RGM: 123456789");
        photoImageView.setImageResource(R.drawable.developer_photo); // Ensure you have a photo in drawable
    }
}