package javabeans;

import java.io.Serializable;
import java.util.Objects;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Version;

@Entity
public class Enfermaria implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(length = 25, nullable = false)
    private String lugar;
    
    @Column(nullable = false)
    private int quantidadeLeitos;
    
    @Version
    private int versao;

    public Enfermaria() {
        this.id = 0L;
        this.lugar = "";
        this.quantidadeLeitos = 0;
        this.versao = 0;
    }
    
    

    public Enfermaria(Long id, String lugar, int quantidadeLeitos, int versao) {
        this.id = id;
        this.lugar = lugar;
        this.quantidadeLeitos = quantidadeLeitos;
        this.versao = versao;
    }
    
    

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 29 * hash + Objects.hashCode(this.id);
        hash = 29 * hash + Objects.hashCode(this.lugar);
        hash = 29 * hash + this.quantidadeLeitos;
        hash = 29 * hash + this.versao;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Enfermaria other = (Enfermaria) obj;
        if (this.quantidadeLeitos != other.quantidadeLeitos) {
            return false;
        }
        if (this.versao != other.versao) {
            return false;
        }
        if (!Objects.equals(this.lugar, other.lugar)) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        return true;
    }

    
    
    public String getLugar() {
        return lugar;
    }

    public void setLugar(String lugar) {
        this.lugar = lugar;
    }

    public int getQuantidadeLeitos() {
        return quantidadeLeitos;
    }

    public void setQuantidadeLeitos(int quantidadeLeitos) {
        this.quantidadeLeitos = quantidadeLeitos;
    }

    public int getVersao() {
        return versao;
    }

    public void setVersao(int versao) {
        this.versao = versao;
    }
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return this.lugar;
    }
    
}
