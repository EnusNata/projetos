package com.example.tema_05;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setTitle("Hello World");
    }

    public void msgBoasVindas(View view){
        TextView textMensagem = findViewById(R.id.Textmensagem);
        textMensagem.setText("seja bem-vindo");
    }
}