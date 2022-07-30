package com.example.tema_08_1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.text.DecimalFormat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myButtonListenerMethod();

        setTitle("Calculadora de IMC");
    }

    public void myButtonListenerMethod(){

        Button btnCalcular = findViewById(R.id.buttonCalcular);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                //  Variaveis obtidas do layout (string)
                EditText editMassa = findViewById(R.id.editMassa);
                EditText editAltura = findViewById(R.id.editAltura);
                EditText editImc = findViewById(R.id.editImc);

                //  Variaveis numericas para realizar o calculo (double)
                Double massa = Double.parseDouble(editMassa.getText().toString());
                Double altura = Double.parseDouble(editAltura.getText().toString());

                Double imc = (massa) / (altura * altura);

                //  Formatar e mostrar numero de casas decimais
                DecimalFormat df = new DecimalFormat("#.#");
                editImc.setText(df.format(imc).toString());

                //  Categorizar IMC
                String categoria;

                if(imc < 15)
                    categoria = "Muito severamente abaixo do peso";
                else if(imc < 16)
                    categoria = "Severamente abaixo do peso";
                else if(imc < 18.5)
                    categoria = "Abaixo do peso";
                else if(imc < 25)
                    categoria = "Normal";
                else if(imc < 30)
                    categoria = "Sobrepeso";
                else if(imc < 35)
                    categoria = "Moderadamente obeso";
                else if(imc < 40)
                    categoria = "Severamente obeso";
                else
                    categoria = "Muito severamente obeso";

                //  Informar imc
                TextView textCategoria = findViewById(R.id.textCategoria);
                textCategoria.setText(categoria);
            }
        });
    }
}