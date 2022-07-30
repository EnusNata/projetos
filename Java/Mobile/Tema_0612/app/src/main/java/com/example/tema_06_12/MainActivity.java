package com.example.tema_06_12;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText editPrecoAlcool;
    EditText editPrecoGasolina;
    TextView textResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setTitle("Alcool ou Gasolina");

        editPrecoAlcool = findViewById(R.id.editPrecoAlcool);
        editPrecoGasolina = findViewById(R.id.editPrecoGasolina);
        textResultado = findViewById(R.id.textResultado);
    }

    public void calcularPreco(View view){
        Double PrecoAlcool = Double.parseDouble(editPrecoAlcool.getText().toString());
        Double PrecoGasolina = Double.parseDouble(editPrecoGasolina.getText().toString());

        Double Resultado = PrecoAlcool/PrecoGasolina;

        if (Resultado >= 0.7){
            textResultado.setText("Melhor utilizar gasolina");
        }
        else{
            textResultado.setText("Melhor utilizar alcool");
        }
    }
}