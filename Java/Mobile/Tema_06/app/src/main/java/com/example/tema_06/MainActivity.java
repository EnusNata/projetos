package com.example.tema_06;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setTitle("Jogo do número");
    }

    public void resultado(View view){
        TextView textResultado = findViewById(R.id.TextResultado);
        int resultado = new Random().nextInt(11);
        textResultado.setText("O número é: " + resultado);
    }
}